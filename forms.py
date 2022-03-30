from wtforms import Form, StringField, PasswordField, validators

class LoginForm(Form):
    username = StringField('Username', [
        validators.Length(min=4, max=25),
        validators.DataRequired()
        ])
    password = PasswordField('Password', [
        validators.DataRequired()
        ])

class NewPostForm(Form):
    title = StringField('Title', [
        validators.DataRequired(),
        validators.Length(min=4, max=30)
    ])
    body = StringField('Post', [
        validators.DataRequired(),
        validators.Length(min=4)
    ])
    tags = StringField('Tags', [
        validators.Length(max=20)
    ])

if __name__=='__main__':
    pass