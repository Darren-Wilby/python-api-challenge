import React, { useState, useEffect } from 'react';

const Typewriter = ({ text, delay }) => {
    // State variables for current text and current index
    const [currentText, setCurrentText] = useState('');
    const [currentIndex, setCurrentIndex] = useState(0);

    // useEffect hook to manage typewriter animation effect
    useEffect(() => {
        if (currentIndex < text.length) {
            // Set a timeout to update the current text and index with a delay
            const timeout = setTimeout(() => {
                setCurrentText(prevText => prevText + text[currentIndex]);
                setCurrentIndex(prevIndex => prevIndex + 1);
            }, delay);

            // Cleanup function to clear the timeout on component unmount or re-render
            return () => clearTimeout(timeout);
        }
    }, [currentIndex, delay, text]); // Dependencies for the useEffect hook

    return <span>{currentText}</span>;
};

export default Typewriter;