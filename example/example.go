//
// Code này phòng trường hợp
// 1. Bạn Lê Hồng Sơn quá ngooo để impl
// 2. Xem 1
// 3. Xem lại 2
//

package main

import (
	"bytes"
	"fmt"
	"io"
	"mime/multipart"
	"net/http"
	"os"
	"path/filepath"
)

func doDetectScene(imagePath string) string {
	fmt.Println("Processing file:", filepath.Base(imagePath))

	file, _ := os.Open(imagePath)
	defer file.Close()

	var body bytes.Buffer
	writer := multipart.NewWriter(&body)
	part, _ := writer.CreateFormFile("image", filepath.Base(imagePath))
	io.Copy(part, file)
	writer.Close()

	req, _ := http.NewRequest("POST", "http://localhost:8000/detect_scene", &body)
	req.Header.Set("Content-Type", writer.FormDataContentType())

	client := &http.Client{}
	resp, _ := client.Do(req)
	respBody, _ := io.ReadAll(resp.Body)

	if bytes.Contains(respBody, []byte(`"status":true`)) { return string(respBody) } else { return "" }
}
