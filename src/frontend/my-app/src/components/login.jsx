import './Login.css'

export default function Login()
{
    return (
    <>
    <form method="post">
        <input type="text" name="username" id="username"  placeholder="Username"/>
        <input type="text" name="password" id="password"  placeholder="Password"/>
        <input type="submit" value="Submit"/>
    </form>
    </>
    )
}