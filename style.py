css = """
.container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(7.5rem, 1fr)); /* Responsive grid */
    gap: .5rem;
    width:650px;
}
.card {
    border: 1px solid #00000069;
    padding: 15px;
    border-radius: 3px;
    /* box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); */
}
.card ul {
    list-style: none;
    padding: 0;
}
.card h3 {
    margin-top: 0;
}
"""