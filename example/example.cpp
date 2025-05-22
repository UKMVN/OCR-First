//
// Code này phòng trường hợp
// 1. Bạn Lê Hồng Sơn quá ngooo để impl
// 2. Xem 1
// 3. Xem lại 2
//

#include <iostream>
#include <curl/curl.h>
#include <filesystem>

std::string do_detect_scene(const std::string& imagePath)
{
    std::cout << "Processing file: " << std::filesystem::path(imagePath).filename() << std::endl;

    CURL* curl = curl_easy_init();
    if (!curl) return "";

    curl_mime* mime = curl_mime_init(curl);
    curl_mimepart* part = curl_mime_addpart(mime);
    curl_mime_name(part, "image");
    curl_mime_filedata(part, imagePath.c_str());

    curl_easy_setopt(curl, CURLOPT_URL, "http://localhost:8000/detect_scene");
    curl_easy_setopt(curl, CURLOPT_MIMEPOST, mime);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, NULL);

    std::string response;
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);

    CURLcode res = curl_easy_perform(curl);
    curl_mime_free(mime);
    curl_easy_cleanup(curl);

    return (res == CURLE_OK && response.find("\"status\":true") != std::string::npos) ? response : "";
}
