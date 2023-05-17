use crate::config::COLOR;
use crate::command::ShardManagerContainer;
use serenity::builder::{CreateApplicationCommand, CreateEmbed};
use serenity::client::bridge::gateway::ShardId;
use serenity::client::Context;
use serenity::model::prelude::interaction::application_command::ApplicationCommandInteraction;
use serenity::model::prelude::interaction::InteractionResponseType;
use tokio::time::Instant;

pub fn data(data: &mut CreateApplicationCommand) -> &mut CreateApplicationCommand {
    return data
        .name("ping")
        .description("API 레이턴시를 확인할 수 있어요");
}

pub async fn execute(_command: ApplicationCommandInteraction, _ctx: Context) {
    let data = _ctx.data.read().await;
    let shard_manager = match data.get::<ShardManagerContainer>() {
        Some(v) => v,
        None => {
            println!("There was a problem getting the shard manager");
            return;
        }
    };
    let manager = shard_manager.lock().await;
    let runners = manager.runners.lock().await;
    let runner = match runners.get(&ShardId(_ctx.shard_id)) {
        Some(runner) => runner,
        None => {
            println!("No shard found");
            return;
        }
    };

    let time = Instant::now();
    let _ = _command
        .create_interaction_response(&_ctx.http, |r| {
            r.kind(InteractionResponseType::ChannelMessageWithSource)
                .interaction_response_data(|message| {
                    message.embed(|e| {
                        e.title(":hourglass_flowing_sand: **Measuring...**");
                        e.description("Just hold on sec...");
                        e.color(0x0D0D0D);
                        e.footer(|f| {
                            f.text(_command.user.tag());
                            f.icon_url(_command.user.avatar_url().unwrap())
                        });

                        return e;
                    })
                })
        })
        .await;

    let latency = runner.latency;
    let elapsed_time = time.elapsed();
    let mut embed = CreateEmbed::default();
    embed.title(":ping_pong: **Pong!**");
    embed.description(format!(
        "**BOT:** {:?}**ms**\n**API:** {:?}**ms**",
        elapsed_time.as_millis(),
        latency.unwrap_or_default().as_millis()
    ));
    embed.color(COLOR);
    embed.footer(|f| {
        f.text(_command.user.tag());
        f.icon_url(_command.user.avatar_url().unwrap())
    });

    let _ = _command
        .edit_original_interaction_response(&_ctx.http, |r| r.add_embed(embed))
        .await;
}