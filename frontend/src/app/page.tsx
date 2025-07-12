(
echo export default function Home() {
echo   const fetchData = async () => {
echo     const res = await fetch('http://localhost:3001/api');
echo     const data = await res.json();
echo     console.log(data);
echo   };
echo 
echo   return (
echo     <main className="p-4">
echo       <h1 className="text-2xl font-bold">Dream Arc Fullstack</h1>
echo       <button 
echo         onClick={fetchData}
echo         className="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
echo       >
echo         Test Backend Connection
echo       </button>
echo     </main>
echo   );
echo }
) > frontend/src/app/page.tsx