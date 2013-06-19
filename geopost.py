import web

urls = (
	"/post/add", "postadd",
	"/post/get/([0-9]+)", "postget",
	"/post/list", "postlist"
)

app = web.application(urls, globals())

if __name__ == "__main__":
	app.run()
