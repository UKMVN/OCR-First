//
// Code này phòng trường hợp
// 1. Bạn Lê Hồng Sơn quá ngooo để impl
// 2. Xem 1
// 3. Xem lại 2
//

const fs = require('fs');
const axios = require('axios');
const FormData = require('form-data');
const path = require('path');

async function doDetectScene(imagePath)
{
    console.log("Processing file:", path.basename(imagePath));
    const form = new FormData();
    form.append('image', fs.createReadStream(imagePath));

    const response = await axios.post('http://localhost:8000/detect_scene', form, { headers: form.getHeaders() });
    return response.data.status ? response.data.result : "";
}
