<template>
    <div>

        
        

    </div>
</template>

<script>
    export default {

        data() {
            return {
<<<<<<< HEAD
                form_data: []
=======
                form_data: {
                    name: "",
                    max_width: null,
                    max_height: null,
                    max_depth: null,
                    user: null
                }
>>>>>>> fa23ae6... [fix]403解消
            }
        },
        
        async mounted () {



                    const requestOptions = {
                    method: "GET",
<<<<<<< HEAD
                        headers: { "Authorization": "Token " + this.$store.state.UserKey },
=======
                    headers: { "Content-Type": "application/json" },
>>>>>>> fa23ae6... [fix]403解消
                }


                fetch('http://127.0.0.1:8000/api/v1/printer3d/', requestOptions)
                    .then(response => response.json())
                    .then((data) => {
                      console.log(data);
                    });









            },
  


    }
</script>

<style scoped>
</style>
