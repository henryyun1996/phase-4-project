import React from 'react';
import { Segment, Grid, Form, Button } from 'semantic-ui-react';
import { useFormik } from 'formik';
import * as yup from 'yup';
import { useHistory } from 'react-router-dom';

const EditProfile = ({ user, setUser }) => {
  const history = useHistory();
  console.log(user)

  const initialValues = {
    username: '',
    password: '',
  };

  const validationSchema = yup.object({
    username: yup.string().required('Please enter a username'),
    password: yup
      .string()
      .min(6, 'Password must be at least 6 characters')
      .max(20, 'Password must be 20 characters or less'),
  });

  const onSubmit = (values) => {
    fetch(`/user/${user.id}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: values.username,
        _password_hash: values.password,
      }),
    })
      .then((res) => {
        if (res.ok) {
          return res.json();
        }
        throw new Error('Network response was not ok');
      })
      .then((data) => {
        setUser(data);
        history.push('/');
      })
      .catch((error) => {
        console.error(error);
      });
  };

  const formik = useFormik({
    initialValues,
    validationSchema,
    onSubmit,
  });

  return (
    <div id="editprofile">
      <Segment secondary>
        <Grid>
          <Grid.Column verticalAlign='middle'>
            <Form onSubmit={formik.handleSubmit}>
              <h1>Edit Login Credentials</h1>
              <Form.Field>
                <label>New Username</label>
                <Form.Input
                  name='username'
                  type='text'
                  placeholder='Username'
                  value={formik.values.username}
                  onChange={formik.handleChange}
                />
                {formik.touched.username && formik.errors.username ? (
                  <p style={{ color: '#ff0000' }}>{formik.errors.username}</p>
                ) : null}
              </Form.Field>
              <br />
              <Form.Field>
                <label>New Password</label>
                <Form.Input
                  name='password'
                  type='password'
                  placeholder='Password'
                  value={formik.values.password}
                  onChange={formik.handleChange}
                />
                {formik.touched.password && formik.errors.password ? (
                  <p style={{ color: '#ff0000' }}>{formik.errors.password}</p>
                ) : null}
              </Form.Field>
              <br />
              <Button className='ui button' type='submit'>
                Update Credentials
              </Button>
            </Form>
          </Grid.Column>
        </Grid>
      </Segment>
    </div>
  );
};

export default EditProfile;