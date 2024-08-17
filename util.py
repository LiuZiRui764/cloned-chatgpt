from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
def generate_script(subject,video_length,creativity,api_key):
    title_template = ChatPromptTemplate.from_messages(
        [
            ("human","请为'{subject}'这个主题的视频想一个吸引人的标题")
        ]
    )
    script_template = ChatPromptTemplate.from_messages(
        [
            ("human",
             """你是一位短视频博主。根据以下标题和相关的信息，为短视频写一个短视频的脚本。
             视频标题:{title},视频时长：{video_length}分钟,生成的脚本的长度需要符合视频时长。
             要求：
             开头能抓住读者的眼球，中间能提供干货内容，结尾有惊喜，脚本格式按照【开头，中间，结尾】的方式分隔。
             整体内容需要轻松有趣，能吸引年轻人。
             """)
        ]
    )
    model = ChatOpenAI(openai_api_key = api_key,
                       temperature=creativity,
                       openai_api_base = "https://api.aigc369.com/v1")
    title_chain = title_template|model
    script_chain = script_template|model
    title = title_chain.invoke({"subject":subject}).content
    script = script_chain.invoke({"title":title,"video_length":video_length}).content
    return title,script
print(generate_script(" 第五人格",1,0.7, os.getenv("OPENAI_API_KEY")))

