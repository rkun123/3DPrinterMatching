<template>
    <div>

        
        

    </div>
</template>

<script>
    export default {

        data() {
            return {
                form_data: {
                    name: "",
                    max_width: null,
                    max_height: null,
                    max_depth: null,
                    user: null
                }
            }
        },
        
        async mounted () {



                    const requestOptions = {
                    method: "GET",
                    headers: { "Content-Type": "application/json" },
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
