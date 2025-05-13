export default function QuizCard({ question, options, correct_option }) {
    const [selectedOption, setSelectedOption] = useState(null);
    const [isSubmitted, setIsSubmitted] = useState(false);
  
    const handleSubmit = () => {
      setIsSubmitted(true);
    };
  
    return (
      <div className="quiz-card">
        <h3>Quiz Question</h3>
        <p>{question}</p>
        
        <div className="options">
          {options.map((option, index) => (
            <div 
              key={index}
              className={`option 
                ${selectedOption === option ? 'selected' : ''}
                ${isSubmitted && option === correct_option ? 'correct' : ''}
                ${isSubmitted && selectedOption === option && option !== correct_option ? 'incorrect' : ''}
              `}
              onClick={() => !isSubmitted && setSelectedOption(option)}
            >
              {option}
            </div>
          ))}
        </div>
  
        {!isSubmitted ? (
          <button onClick={handleSubmit} disabled={!selectedOption}>
            Submit Answer
          </button>
        ) : (
          <div className="result">
            {selectedOption === correct_option 
              ? "Correct! 🎉" 
              : `Incorrect. The correct answer is: ${correct_option}`}
          </div>
        )}
      </div>
    );
  }