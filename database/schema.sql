CREATE DATABASE IF NOT EXISTS recommendation_system;
USE recommendation_system;

-- =========================
-- USERS
-- =========================
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(32) NOT NULL UNIQUE,
    gender VARCHAR(16),
    age INT,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- MOVIES
-- =========================
CREATE TABLE IF NOT EXISTS movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tmdb_id INT UNIQUE,
    title VARCHAR(128) NOT NULL,
    genres JSON,
    overview TEXT,
    release_date DATE,
    vote_average DECIMAL(3,2),
    vote_count INT,
    runtime INT,
    tagline VARCHAR(256),
    director VARCHAR(64),
    cast JSON,
    poster_path VARCHAR(64),
    backdrop_path VARCHAR(64)
);

-- =========================
-- RATINGS
-- =========================
CREATE TABLE IF NOT EXISTS ratings (
    user_id INT,
    movie_id INT,
    rating DECIMAL(2,1) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, movie_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (movie_id) REFERENCES movies(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- =========================
-- PERSONALITIES
-- =========================
CREATE TABLE IF NOT EXISTS personalities (
    user_id INT PRIMARY KEY,
    openness DECIMAL(3,2) NOT NULL,
    conscientiousness DECIMAL(3,2) NOT NULL,
    extraversion DECIMAL(3,2) NOT NULL,
    agreeableness DECIMAL(3,2) NOT NULL,
    neuroticism DECIMAL(3,2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);
