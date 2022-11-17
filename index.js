const MYSERNER = 'https://test-g7s0.onrender.com/'

const HomePage = async () =>{
    res = await fetch(`${MYSERNER}`).then((response) => response.json())
    console.log(res)
}

HomePage()