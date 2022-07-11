class Message:
    
    def botnoi_payload(line_message_func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            return {
                "response_type": "object",
                "line_payload": [line_message_func(*args, **kwargs)]
            }
        return wrapper

    @classmethod
    @botnoi_payload
    def text_message(cls, text: str):
        return {"type": "text","text": text}

    @classmethod
    @botnoi_payload
    def flex_message(cls, flexdata: dict):
        return {
            "type": "flex",
            "altText": "this is a flex message",
            "contents": flexdata
            }
  
    @classmethod
    @botnoi_payload
    def image_message(cls, original_image_url: str, preview_image_url: str):
        return {
                "type": "image",
                "originalContentUrl": original_image_url,
                "previewImageUrl": preview_image_url
            }


class Sequential(dict):
    
    def __init__(self, *messages) -> None:
        self.messages = [message["line_payload"][0] for message in messages]
        
        
    def __repr__(self) -> dict:
        self.__setitem__("response_type", "object")
        self.__setitem__("line_payload", self.messages)
        return super().__repr__()
    
    def to_dict(self):
        return {
            "response_type": "object",
            "line_payload": self.messages
        }
        
    
    # def botnoi_payload(line_payload_func, *args, **kwargs):
    #     def wrapper(*args, **kwargs):
    #         return {
    #             "response_type": "object",
    #             "line_payload": line_payload_func(*args, **kwargs)
    #         }
    #     return wrapper
        
    

if __name__=='__main__':
    print(Message.text_message("สวัสดีครับ"))
    print(Message.image_message("o", "p"))
    
    messages = Sequential(
        Message.text_message("สวัสดีครับ"),
        Message.text_message("วันนี้เป็นไงบ้างครับ"),
        Message.image_message("https://quotepark.com/media/authors/prayut-chan-o-cha.jpeg", "https://quotepark.com/media/authors/prayut-chan-o-cha.jpeg"),
    ).to_dict()
    

    print(messages)
