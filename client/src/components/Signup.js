import React from 'react'
import { Button, Form } from 'semantic-ui-react'
import { useFormik } from "formik";
import * as yup from "yup";
import { useHistory } from "react-router-dom";

const Signup = ({ setUser }) => {
    const history = useHistory();

    const formSchema = yup.object().shape({
        username: yup.string()
            .required('Required')
            .min(5, 'Username needs to be at least 5 characters long.')
            .max(15, 'Username can be at most 15 characters long.')
            .required('Required'),
        password: yup.string()
            .required('No password provided.') 
            .min(5, 'Password is too short - should be 5 characters minimum.')
            .matches(/[\d\w]/, 'Password can only contain letters and numbers.'),
        confirm_password: yup.string()
            .oneOf([yup.ref("password")], "Passwords do not match")
            .required("Password Confirm is required"),
      })

    const formik = useFormik({
        initialValues: {
            username: '',
            password: ''
        },
        validationSchema: formSchema,
        onSubmit: (values) => {
            console.log("Creating a user...")
            if (formik.isValid) {
                fetch('/signup', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(values)
                }).then(res => {
                    if (res.ok) {
                        res.json().then( new_user => setUser(new_user))
                        console.log("User successfully created!")
                        history.push('/home')
                    } else {
                        res.json().then( err => {
                            console.log(err)
                            alert('Oops, username is already taken. Please choose another one.')
                        })
                    }
                }).catch(err => {
                    console.error('Error during fetch:', err);
                });
            }
        }
    })

  return (
    <div>
        <h1>Sign up Form</h1>
        <Form onSubmit={formik.handleSubmit} style={{ margin: "30px" }}>
            <Form.Field validate>
                <label>Username</label>
                <input 
                    type="text"
                    name="username"
                    placeholder='Username' 
                    value={formik.values.username}
                    onChange={formik.handleChange}
                />
                <p style={{ color: "purple" }}> {formik.errors.username}</p>

            </Form.Field>
            <Form.Field validate>
                <label>Password</label>
                <input 
                    id="password"
                    name="password"
                    type="password"
                    placeholder='Password' 
                    value={formik.values.password}
                    onChange={formik.handleChange}
                />
                <p style={{ color: "purple" }}> {formik.errors.password}</p>
            </Form.Field>
            <Form.Field validate>
                <label>Confirm Password</label>
                <input 
                    id="confirm-password"
                    name="confirm_password"
                    type="password"
                    placeholder='Confirm password' 
                    onChange={formik.handleChange}
                    value={formik.values.confirm_password}
                />
                <p style={{ color: "purple" }}> { formik.errors.confirm_password }</p>
            </Form.Field>
            <Button
              className='ui button' 
              onClick={formik.handleSubmit}
              type='submit'>Sign Up</Button>
        </Form>
    </div>
  )
}

export default Signup