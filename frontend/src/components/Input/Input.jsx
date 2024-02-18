import './Input.css'

function Input({ label, type, placeholder, value, onChange, autocapitalize = "off" }) {
  return (
    <>
      {(label) ? <label>{label}</label> : null}
      <input
          type={type}
          placeholder={placeholder}
          value={value}
          onChange={onChange}
          className="darmaInput"
          autoCapitalize={autocapitalize}
        />
    </>
  )
}

export default Input
