class StudentRouter(BaseHTTPRequestHandler):
    def do_Get(self):
        # path = urlpare(self.path).path

        # if path in ("/", "/index.html"):

        #     return serve(self)
        #     if path.startswith("/static/")
        #     return serve_static(self)

        #     if path == "/api/students":
        #         return get_all_students(self)

                if path.startswith("/api/students/":
                    student_id = int(path.split("/")[-1])
                    return get_student_(self, student_id)

                    return send_404(self)