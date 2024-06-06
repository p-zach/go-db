# go-db

Open API access 70,210 Go .SGF games. Sourced from [https://homepages.cwi.nl/~aeb/go/games/games/index.html](https://homepages.cwi.nl/~aeb/go/games/games/index.html); more information about the games can be found there.

To fetch a game by name, search `https://p-zach.github.io/go-db/all_games.json` for the game you want and then fetch it from
`https://p-zach.github.io/go-db/games_named/[game_name].sgf`.

To fetch a game by index (useful for picking one at random), fetch `https://p-zach.github.io/go-db/games_indexed/[0..70209].sgf`.