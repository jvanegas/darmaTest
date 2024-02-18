import './Button.css';

function Button ({ children, onClick }) {
  return (
    <button className="darmaButton" onClick={onClick}>{children}</button>
  )
}

export default Button;
