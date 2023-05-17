pub mod ping;

use serenity::model::application::command::Command;
use serenity::model::application::interaction::Interaction;
use serenity::client::bridge::gateway::ShardManager;
use serenity::prelude::*;
use std::sync::Arc;

pub struct ShardManagerContainer;

impl TypeMapKey for ShardManagerContainer {
    type Value = Arc<Mutex<ShardManager>>;
}

pub async fn executor(_ctx: Context, interact: Interaction) {
    if let Interaction::ApplicationCommand(command) = interact {
        let _content = match command.data.name.as_str() {
            "ping" => ping::execute(command, _ctx).await,
            _ => return,
        };
    }
}

pub async fn register(_ctx: Context) {
    let _ = Command::create_global_application_command(&_ctx.http, |c| ping::data(c)).await;
}
