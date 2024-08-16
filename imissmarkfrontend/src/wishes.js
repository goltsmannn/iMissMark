import axios from "axios";
import {useEffect, useState} from "react";


function Wishes () {
    const [wishes, setWishes] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/wishes")
        .then(response => {
            setWishes(response.data);
        })
            .catch(error => {
                console.error(error);
            })
    }, [])


    return(
        wishes.map(wish => {
            return (
                <>
                <h1>{wish.author}</h1>
                <div>
                    <p>{wish.text}</p>
                    <p>{wish.publication_date}</p>
                </div>
            </>);
        })
    );
}

export default Wishes;