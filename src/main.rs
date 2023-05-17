pub mod command;
pub mod config;
pub mod event;

extern crate dotenv;

use command::ShardManagerContainer;
use dotenv::dotenv;
use serenity::{Client, prelude::GatewayIntents};
use std::{env, sync::Arc};

#[tokio::main]
async fn main() {
    dotenv().ok();
    let token = env::var("TOKEN").expect("TOKEN value is null");
    let intents = GatewayIntents::GUILD_MESSAGES
        | GatewayIntents::DIRECT_MESSAGES
        | GatewayIntents::MESSAGE_CONTENT;
    
    let mut client = Client::builder(&token, intents)
        .event_handler(event::Handler)
        .await.expect("expect error for creating client");
    {
        let mut data = client.data.write().await;
        data.insert::<ShardManagerContainer>(Arc::clone(&client.shard_manager));
    }

    if let Err(why) = client.start().await {
        println!("client error: {:?}", why);
    }
}
