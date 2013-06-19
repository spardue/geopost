import web
from postcontroller import PostController

urls = (
	"/post", "PostController",
)


app = web.application(urls, globals())




if __name__ == "__main__":
	app.run()