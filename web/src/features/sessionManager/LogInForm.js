import React from 'react'
import { Field, reduxForm } from 'redux-form'

let logInForm = props => {
  const { handleSubmit } = props
  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="username">Username</label>
        <Field name="username" component="input" type="text" />
      </div>
      <div>
        <label htmlFor="password">Password</label>
        <Field name="password" component="input" type="password" />
      </div>
      <div>
        <label htmlFor="serverAddress">serverAddress</label>
        <Field name="serverAddress" component="input" type="text" />
      </div>
      <button type="submit">Submit</button>
    </form>
  )
}

let LogInForm = reduxForm({
  // a unique name for the form
  form: 'logIn'
})(logInForm)

export default LogInForm