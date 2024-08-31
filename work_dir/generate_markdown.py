# filename: generate_markdown.py
from skills import generate_and_save_markdown

sections = [
    {
        "title": "AI News",
        "level": "h1",
        "content": "This week in AI news, we have a lot of updates from the world of AI image generation. Mid Journey has opened up their free trial again, and Idiogram has rolled out a new model called Idiogram 2.0. We also have updates from Luma Labs, Hot Shot, and more.",
    },
    {
        "title": "Mid Journey Free Trial",
        "level": "h2",
        "content": "Mid Journey has opened up their free trial again, allowing users to generate 25 images for free. After the free trial, users will have to pay for the service. Mid Journey is still one of the best AI image generation platforms, and this is a great opportunity for new users to try it out.",
    },
    {
        "title": "Idiogram 2.0",
        "level": "h2",
        "content": "Idiogram has rolled out a new model called Idiogram 2.0. This model is available to all users for free, and it is capable of generating high-quality images. Idiogram is known for its ability to generate text inside of images, and this new model is no exception.",
    },
    {
        "title": "Luma Labs",
        "level": "h2",
        "content": "Luma Labs has released a new version of their AI video generation tool called Dream Machine 1.5. This tool is capable of generating high-quality videos, and it has a number of new features such as higher quality text to video and smarter understanding of prompts.",
    },
    {
        "title": "Hot Shot",
        "level": "h2",
        "content": "Hot Shot is a new AI video generation tool that has been released this week. This tool is capable of generating high-quality videos, but it is still in its early stages and has some limitations. Users can generate two videos for free every day, or they can pay $100 per month to generate more videos.",
    },
    {
        "title": "Perplexity",
        "level": "h2",
        "content": "Perplexity is a search engine that uses AI to generate answers to user queries. This week, Perplexity has rolled out a new feature called code interpreter, which allows users to write code and have it executed by the AI. This feature is still in its early stages, but it has a lot of potential.",
    },
    {
        "title": "HubSpot",
        "level": "h2",
        "content": "HubSpot has released a new bundle of resources for using ChatGPT at work. This bundle includes a number of templates and guides for using ChatGPT to improve productivity and efficiency. It also includes a checklist for adopting AI in the workplace.",
    },
    {
        "title": "Open AI",
        "level": "h2",
        "content": "Open AI has partnered with Condé Nast to make content from their brands available inside of Open AI and ChatGPT. This partnership will allow users to access a wide range of content from brands such as Vogue, The New Yorker, and more.",
    },
    {
        "title": "Microsoft",
        "level": "h2",
        "content": "Microsoft has released a new model called F3.5, which has 3.82 billion parameters. This model is designed to run on mobile devices and is smaller than other models. Microsoft has also announced that they will be releasing a new feature called Recall AI, which will allow users to search for information on their computer.",
    },
    {
        "title": "Robotics",
        "level": "h2",
        "content": "There have been a number of updates in the world of robotics this week. Unry Robotics has released a new robot called the G1, which is capable of walking up and down stairs and jumping. AGI Bot has also released a new robot that is capable of challenging Elon Musk's Optimus robot.",
    },
    {
        "title": "Conclusion",
        "level": "h2",
        "content": "That's all for this week's AI news. We have seen a number of updates from the world of AI image generation, video generation, and more. We have also seen a number of new tools and features released, including Perplexity's code interpreter and HubSpot's bundle of resources for using ChatGPT at work.",
    },
]

generate_and_save_markdown(sections, output_file="ai_news.md", report_title="AI News")