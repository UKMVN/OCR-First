//
// Code này phòng trường hợp
// 1. Bạn Lê Hồng Sơn quá ngooo để impl
// 2. Xem 1
// 3. Xem lại 2
//

import java.io.*;
import java.net.http.*;
import java.net.URI;
import java.nio.file.*;

public class SceneDetector
{
    public static String doDetectScene(String imagePath) throws Exception
    {
        System.out.println("Processing file: " + Path.of(imagePath).getFileName());

        HttpRequest.BodyPublisher body = HttpRequest.BodyPublishers.ofFile(Path.of(imagePath));
        HttpRequest request = HttpRequest.newBuilder()
            .uri(new URI("http://localhost:8000/detect_scene"))
            .header("Content-Type", "multipart/form-data")
            .POST(body)
            .build();

        HttpResponse<String> response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
        return response.body().contains("\"status\":true") ? response.body() : "";
    }
}
