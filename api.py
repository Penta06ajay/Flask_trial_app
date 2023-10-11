import paralleldots

paralleldots.set_api_key("Dd6AlzfcBb7AKWR6i6FcT3ys056rJxfwrqJdrGPwnQ8")

def ner(text):
    ner = paralleldots.ner(text)
    return ner