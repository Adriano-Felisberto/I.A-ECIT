class MovieRecommendationAgent:
    def __init__(self):
        self.user_ratings = {}
        self.movie_database = {
            "Matrix": ["Ação", "Ficção Científica"],
            "Inception": ["Ação", "Ficção Científica"],
            "The Social Network": ["Drama"],
            # ... (mais filmes e gêneros)
        }

    def collect_user_ratings(self):
        print("Bem-vindo ao sistema de recomendação de filmes!")
        print("Por favor, avalie alguns filmes (de 1 a 5):")
        for movie in self.movie_database:
            while True:
                try:
                    rating = float(input(f"Qual a sua avaliação para '{movie}'? (1 a 5): "))
                    if 1 <= rating <= 5:
                        self.user_ratings[movie] = rating
                        break
                    else:
                        print("Por favor, insira uma avaliação entre 1 e 5.")
                except ValueError:
                    print("Entrada inválida. Insira um número válido.")

    def recommend_movie(self):
        # Calcula a média das avaliações do usuário
        avg_rating = sum(self.user_ratings.values()) / len(self.user_ratings)

        # Filtra filmes que o usuário ainda não avaliou
        unrated_movies = [movie for movie in self.movie_database if movie not in self.user_ratings]

        # Recomenda filmes com base nos gêneros preferidos do usuário
        recommended_movies = []
        for movie in unrated_movies:
            genres = self.movie_database[movie]
            if any(genre in self.user_ratings for genre in genres):
                recommended_movies.append(movie)

        return recommended_movies

# Exemplo de uso
agent = MovieRecommendationAgent()
agent.collect_user_ratings()
recommended_movies = agent.recommend_movie()
if recommended_movies:
    print("Filmes recomendados:", recommended_movies)
else:
    print("Desculpe, não temos filmes para recomendar com base nas suas avaliações.")
