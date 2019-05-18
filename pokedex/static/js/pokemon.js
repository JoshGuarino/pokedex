class pokemon {
    constructor(poke_json) {
        this.name = poke_json.name;
        this.number = poke_json.number;
        this.weight = poke_json.height;
        this.weight = poke_json.weight;
        this.color = poke_json.color;
        this. description = poke_json.description;
        this.image = "static/images/" + number + '.png';
    }
    getimage() {
        return this.image;
    }
}

module.exports = pokemon;