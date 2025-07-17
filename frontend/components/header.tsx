export default function Header() {
    return (
        <header>
        <h1>Welcome to My App</h1>
        <nav>
            <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/contact">Contact</a></li>
            <li>
                <form method="POST" action="http://localhost:8000/login/" style={{ display: 'inline' }}>
                    <button type="submit">Login</button>
                </form>
            </li>
            </ul>
        </nav>
        </header>
    );
}