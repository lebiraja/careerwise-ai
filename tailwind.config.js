/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        // Streamlit color scheme
        primary: {
          50: '#f0f8ff',
          100: '#e0f2fe',
          200: '#bae6fd',
          300: '#7dd3fc',
          400: '#38bdf8',
          500: '#1f77b4', // Main Streamlit blue
          600: '#1565c0',
          700: '#0d4b8a',
          800: '#0a3d6b',
          900: '#072f52',
        },
        success: {
          50: '#d4edda',
          100: '#c3e6cb',
          500: '#28a745',
          600: '#155724',
        },
        error: {
          50: '#f8d7da',
          100: '#f5c6cb',
          500: '#dc3545',
          600: '#721c24',
        },
        info: {
          50: '#d1ecf1',
          100: '#bee5eb',
          500: '#17a2b8',
          600: '#0c5460',
        },
        warning: {
          50: '#fff3cd',
          100: '#ffeaa7',
          500: '#ffc107',
          600: '#856404',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-out',
        'slide-up': 'slideUp 0.3s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        slideUp: {
          '0%': { opacity: '0', transform: 'translateY(10px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
      },
    },
  },
  plugins: [],
}; 