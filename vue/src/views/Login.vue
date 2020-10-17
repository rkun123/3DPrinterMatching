<template>
    <div>
        LoginPage<br />
        <input v-model="form_data.username" placeholder="edit me">
        <p>Message is: {{ form_data.username }}</p>
        <input v-model="form_data.email" placeholder="edit me">
        <p>Message is: {{ form_data.email }}</p>
        <input v-model="form_data.password" type="password" placeholder="edit me">
        <p>Message is: {{ form_data.password }}</p>


        <button v-on:click="post">Greet</button>
    </div>
</template>

<script>
    export default {

        data() {
            return {
                form_data: {
                    username: '',
                    email: '',
                    password: ''
                }
            }
        },
        methods: {
            post: async function () {
                // メソッド内の `this` は、 Vue インスタンスを参照します
                alert('Hello ' + '!')

                const payload = JSON.stringify(this.form_data)

                const requestOptions = {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: payload
                }

                await fetch('http://127.0.0.1:8000/rest-auth/login/', requestOptions)
                    .then(response => response.json())
                    .then(requestOptions => console.log(requestOptions))

               


            }
        },
          
       
    }

    
</script>  
