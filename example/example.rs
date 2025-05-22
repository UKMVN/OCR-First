//
// Code này phòng trường hợp
// 1. Bạn Lê Hồng Sơn quá ngooo để impl
// 2. Xem 1
// 3. Xem lại 2
//

use reqwest::blocking::Client;
use std::fs::File;
use std::path::Path;

fn do_detect_scene(image_path: &str) -> String {
    println!("Processing file: {}", Path::new(image_path).file_name().unwrap().to_str().unwrap());
    let file = File::open(image_path).unwrap();
    let client = Client::new();

    let res = client.post("http://localhost:8000/detect_scene")
        .multipart(reqwest::blocking::multipart::Form::new()
            .file("image", image_path).unwrap())
        .send().unwrap();

    let body = res.text().unwrap();
    if body.contains("\"status\":true") { body } else { "".into() }
}
