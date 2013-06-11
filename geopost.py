import web
from postadd import postadd

urls = ("/post/add", "postadd")


app = web.application(urls, globals())




if __name__ == "__main__":
	app.run()