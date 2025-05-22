#
# Code này phòng trường hợp
# 1. Bạn Lê Hồng Sơn quá ngooo để impl
# 2. Xem 1
# 3. Xem lại 2
#

require 'net/http'
require 'uri'
require 'mime/types'

def do_detect_scene(image_path)
    puts "Processing file: #{File.basename(image_path)}"
    uri = URI.parse("http://localhost:8000/detect_scene")
    request = Net::HTTP::Post.new(uri)
    form_data = [['image', File.open(image_path)]]
    request.set_form(form_data, 'multipart/form-data')
    response = Net::HTTP.start(uri.hostname, uri.port) { |http| http.request(request) }
    response.body.include?('"status":true') ? response.body : ''
end
