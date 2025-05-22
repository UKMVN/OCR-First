<?php
//
// Code này phòng trường hợp
// 1. Bạn Lê Hồng Sơn quá ngooo để impl
// 2. Xem 1
// 3. Xem lại 2
//

function do_detect_scene($imagePath)
{
    echo "Processing file: " . basename($imagePath) . "\n";

    $cfile = new CURLFile($imagePath);
    $post = ['image' => $cfile];

    $ch = curl_init('http://localhost:8000/detect_scene');
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($ch);
    curl_close($ch);

    return strpos($response, '"status":true') !== false ? $response : "";
}
?>
