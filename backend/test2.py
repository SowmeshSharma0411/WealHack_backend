import base64

with open("./assets/download.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

print(f"Base64 encoded image: {encoded_string}")


def base64_to_jpg(base64_string, output_file):
    # Decode base64 string to bytes
    image_bytes = base64.b64decode(base64_string)

    # Write bytes to a JPG file
    with open(output_file, "wb") as f:
        f.write(image_bytes)


# Example usage
base64_string = "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"  # Your base64 encoded image string here
output_file = "./assets/output.jpg"  # Output JPG file path

base64_to_jpg(base64_string, output_file)
