<div align="center">
  <img src='_docs/imgs/carval-logo.png' width="175">
  <h1><strong>🚗 Carval 💸</strong></h1>
  <h4>Figure out the value of your ride</h4>
  <br/>
  <img src='_docs/imgs/mockup.png' width="500">
</div>

This is a project to demonstrate my abilities in:
* Data Science
* Web Development

In addition, this project was developed using an __agile__ methodology.

## Architecture
### Predictor
The model is deployed as a service using `Flask`. It has only one endpoint:
<table>
  <tbody>
    <tr>
      <th>URL</th>
      <th >Type</th>
      <th>Payload</th>
      <th>Response</th>
    </tr>
    <tr>
      <td><code>127.0.0.1:8080/api</code></td>
      <td>GET</td>
      <td>
<pre><code>
{
    "year_model":   Number,
    "mileage":      Number, 
    "fiscal_power": Number, 
    "fuel_type":    String, 
    "mark":         String
}
</code></pre>
      </td>
      <td>
<pre><code>
{
    "price": Number
}
</code></pre>
      </td>
    </tr>
  </tbody>
</table>

### Client-Side
The client side was developed using `Vue.js`, `vue-router`, and `vuex`.<br>
Furthermore, `Storybook` was used to develop the two main components.

## Project Structure
| Dir        | Desc           |
| ------------- |---------------|
| `app_client`  | old client code. Served through Flask |
| `client_app`  | new client code. Developed as a SPA with `Vue.js` |
| `data`        | where the dataset lives |
| `data_analysis` | 


## Recreate Project
> ##### Recreate the environment
>1. `conda env create -f environment.yml`
>2. `source activate car-prices3.6`

> ##### Launch predictor
>1. `cd app_predictor`
>2. `python app.py &`
> // _The predictor runs on port `8080`_

> ##### Launch Client App
>1. `cd client_app`
>2. `yarn install`
>3. `yarn serve`

> ##### (LEGACY) Launch UI Client
> 1. `cd app_client`
> 2. `python app.py &`
> // _The UI Client runs on port `5000`_

> ##### Access the Application
> Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)
