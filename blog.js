const list = document.querySelector("#blog-list");

fetch("./blog.json")
    .then((response) => response.json())
    .then((posts) => {
        list.replaceChildren();

        for (const post of posts) {
            const item = document.createElement("li");
            const link = document.createElement("a");

            link.href = post.url;
            link.textContent = post.title;
            item.append(link);

            const date = document.createElement("time");
            date.textContent = post.date;
            item.append(" ", date);

            list.append(item);
        }
    })
    .catch(() => {
        list.innerHTML = "<li>記事を読み込めませんでした。</li>";
    });
