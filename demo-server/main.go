package main

import (
	"fmt"
	"net/http"
	"time"

	"github.com/go-chi/chi"
	"github.com/go-chi/chi/middleware"
)

const (
	PORT = 8080
)

type Server struct {
	handler http.Handler
}

func (s *Server) init() {
	r := chi.NewRouter()
	r.Use(middleware.Logger)

	r.Get("/", s.Get)
	r.Post("/", s.Post)

	s.handler = r
}

func (s *Server) Get(w http.ResponseWriter, r *http.Request) {
	time.Sleep(1 * time.Second)
	w.Write([]byte("Get\n"))
}

func (s *Server) Post(w http.ResponseWriter, r *http.Request) {
	time.Sleep(1 * time.Second)
	w.Write([]byte("Post\n"))
}

func main() {
	s := &Server{}
	s.init()
	http.ListenAndServe(fmt.Sprintf(":%d", PORT), s.handler)
}
