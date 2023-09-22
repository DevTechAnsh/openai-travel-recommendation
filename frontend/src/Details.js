export const Detail = ({ data }) => {
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
