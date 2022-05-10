

#![cfg_attr(
  all(not(debug_assertions), target_os = "windows"),
  windows_subsystem = "windows"
)]


use std::process::Command;

fn run_command(command:String) {

Command::new(command).spawn();
}

#[tauri::command]
fn youtube() {
  run_command("youtube".to_string());
    println!("Youtube is called.");
}

#[tauri::command]
fn kodi() {
  run_command("kodi".to_string());
    println!("Kodi is called.");
}

#[tauri::command]
fn bbc() {
  run_command("bbc".to_string());
    println!("BBC is called.");
}

fn main() {
  tauri::Builder::default()
    // This is where you pass in your commands
    .invoke_handler(tauri::generate_handler![youtube,kodi,bbc])
    .run(tauri::generate_context!())
    .expect("failed to run app");
}