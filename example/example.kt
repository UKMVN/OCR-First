//
// Code này phòng trường hợp
// 1. Bạn Lê Hồng Sơn quá ngooo để impl
// 2. Xem 1
// 3. Xem lại 2
//

import java.io.File
import okhttp3.*

fun doDetectScene(imagePath: String): String
{
    println("Processing file: ${File(imagePath).name}")
    val client = OkHttpClient()

    val requestBody = MultipartBody.Builder().setType(MultipartBody.FORM)
        .addFormDataPart("image", File(imagePath).name, RequestBody.create(MediaType.parse("image/*"), File(imagePath)))
        .build()

    val request = Request.Builder()
        .url("http://localhost:8000/detect_scene")
        .post(requestBody)
        .build()

    val response = client.newCall(request).execute().body()?.string() ?: ""
    return if (response.contains("\"status\":true")) response else ""
}
