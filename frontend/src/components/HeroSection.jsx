import React from 'react';
import { useNavigate } from 'react-router-dom';

const HeroSection = ({ backdropPath, imageBaseUrl }) => {
  const navigate = useNavigate();

  const handleGetStarted = () => {
    navigate('/login?mode=register');
  };

  return (
    <div className="relative h-screen w-full overflow-hidden">
      {/* Background Image with Overlay */}
      <div
        className="absolute inset-0 sm-cover bg-center"
        style={{
          backgroundImage: backdropPath 
            ? `url(${imageBaseUrl}/original${backdropPath})`
            : 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
        }}
      >
        <div className="absolute inset-0 bg-gradient-to-b from-slate-900/70 via-slate-900/50 to-slate-900"></div>
      </div>

      {/* Hero Content */}
      <div className="relative h-full flex items-center justify-center px-4">
        <div className="max-w-4xl text-center animate-fade-in">
          <h1 className="text-5xl md:text-7xl font-bold text-white mb-6 leading-tight">
            Bienvenido.
          </h1>
          <p className="text-xl md:text-2xl text-gray-200 mb-4 leading-relaxed">
            Miles de películas. Poco tiempo para explorarlas.
          </p>
          <p className="text-xl md:text-2xl text-gray-200 mb-8 leading-relaxed">
            Deja que la <span className="text-purple-400 font-semibold">inteligencia artificial</span> te recomiende las historias que realmente encajan contigo.
          </p>
          <button 
            onClick={handleGetStarted}
            className="px-8 py-4 bg-purple-600 hover:bg-purple-700 text-white text-lg font-semibold rounded-full transition-all transform hover:scale-105 shadow-lg"
          >
            Comenzar ahora
          </button>
        </div>
      </div>

      <style jsx>{`
        @keyframes fade-in {
          from {
            opacity: 0;
            transform: translateY(20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }

        .animate-fade-in {
          animation: fade-in 1s ease-out;
        }
      `}</style>
    </div>
  );
};

export default HeroSection;