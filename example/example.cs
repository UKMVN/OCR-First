//
// Code này phòng trường hợp
// 1. Bạn Lê Hồng Sơn quá ngooo để impl
// 2. Xem 1
// 3. Xem lại 2
//

using System;
using System.Net.Http;
using System.Threading.Tasks;
using System.IO;

public class SceneDetector
{
    public static async Task<string> DoDetectScene(string imagePath)
    {
        Console.WriteLine("Processing file: " + Path.GetFileName(imagePath));
        using var client = new HttpClient();
        using var content = new MultipartFormDataContent();
        content.Add(new StreamContent(File.OpenRead(imagePath)), "image", Path.GetFileName(imagePath));

        var response = await client.PostAsync("http://localhost:8000/detect_scene", content);
        var json = await response.Content.ReadAsStringAsync();
        return json.Contains("\"status\":true") ? json : "";
    }
}
