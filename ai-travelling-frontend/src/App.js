import './App.css';
import { useMemo, useState } from 'react';
import countryList from 'react-select-country-list';
import Select from 'react-select'


const Details = ({ data }) => {
  return (
    <div className='detail'>
      <table>
        <thead>
          <tr>
            <th>country</th>
            <th>season</th>
            <th>recommendations</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{data?.country}</td>
            <td>{data?.season}</td>
            <td> 
            {data?.recommendations?.map((data) =>  data)}
            </td>
          </tr>
        </tbody>
      </table>
    </div >
  )
}

function App() {
  const [country, setCountry] = useState(null)
  const [data, setData] = useState()
  const [loading, setLoading] = useState()

  const options = useMemo(() => countryList().getData(), [])
  const [seasion, setSeasion] = useState('');
  const [error, setError] = useState('')

  const seasions = [
    { value: 'Summer', label: 'Summer' },
    { value: 'Spring', label: 'Spring' },
    { value: 'Winter', label: 'Winter' },
    { value: 'Rainy', label: 'Rainy' }
  ]


  const handleSubmit = (e) => {
    e.preventDefault()
    fetch(`http://localhost:3000/?country=${country?.label}&season=${seasion?.label}`)
      .then(response => {
        return response.json()
      })
      .then(data => {
        if (data?.detail) {

          setError(data?.detail)
        }
        else setData(data)

      })
      .catch(err => {
        console.log(err)
        setError(err)
      })
  }

  const changeSeason = seasion => {
    setSeasion(seasion)
  };

  const changeHandler = country => {
    setCountry(country)
  }

  return (
    <>
      <div className='App'>
        <h2>Select country and season for recommendations of activities</h2>
        {error && <p style={{ color: 'red' }}>{error}</p>}
        <div className='countries'>
          <small>Select country</small>
          <Select options={options} value={country} onChange={changeHandler} />
        </div>
        <div className='seasons'>
          <small>Select seasion</small>
          <Select options={seasions} value={seasion} onChange={changeSeason} />
        </div>
        <button onClick={handleSubmit}>Submit</button>
      </div>

      {/* // rendering the data fetched by api */}
      {data && <Details data={data} />}
    </>

  )
}

export default App;
