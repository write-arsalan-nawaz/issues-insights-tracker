<script lang="ts">
  import { onMount } from "svelte";
  import Chart from "chart.js/auto";

  let chart: Chart;
  let canvasEl: HTMLCanvasElement;

  onMount(async () => {
    const res = await fetch("http://localhost:8000/stats/open-by-severity");
    const stats = await res.json();

    const labels = Object.keys(stats);
    const data = Object.values(stats);

    chart = new Chart(canvasEl, {
      type: "bar",
      data: {
        labels,
        datasets: [
          {
            label: "# of Open Issues",
            data,
            backgroundColor: "rgba(59, 130, 246, 0.5)", // Tailwind blue-500
            borderColor: "rgba(59, 130, 246, 1)",
            borderWidth: 1,
          },
        ],
      },
    });
  });
</script>

<h1 class="text-2xl font-bold mb-4">Dashboard: Open Issues by Severity</h1>
<canvas bind:this={canvasEl} class="max-w-xl" />
