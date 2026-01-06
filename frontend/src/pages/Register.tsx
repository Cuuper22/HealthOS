const Register = () => {
  return (
    <section className="card">
      <h1>Create Account</h1>
      <form className="form">
        <label>
          First name
          <input type="text" name="firstName" />
        </label>
        <label>
          Last name
          <input type="text" name="lastName" />
        </label>
        <label>
          Email
          <input type="email" name="email" placeholder="you@example.com" />
        </label>
        <label>
          Password
          <input type="password" name="password" />
        </label>
        <button type="submit">Create Account</button>
      </form>
    </section>
  );
};

export default Register;
