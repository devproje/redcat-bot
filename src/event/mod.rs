use serenity::async_trait;
use serenity::model::application::interaction::Interaction;
use serenity::model::gateway::Ready;
use serenity::model::prelude::{Activity};
use serenity::model::user::OnlineStatus;
use serenity::prelude::*;

use crate::command;

pub struct Handler;

#[async_trait]
impl EventHandler for Handler {
    async fn ready(&self, ctx: Context, ready: Ready) {
        let act = Activity::playing(format!("{} {}", ready.user.name, env!("CARGO_PKG_VERSION")));
        ctx.set_presence(Option::from(act), OnlineStatus::Online).await;
        println!("Logged in as {}", ready.user.tag());

        command::register(ctx).await;
    }

    async fn interaction_create(&self, _ctx: Context, _interaction: Interaction) {
        command::executor(_ctx, _interaction).await;
    }
}