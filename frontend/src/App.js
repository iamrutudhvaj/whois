import React, { useState } from 'react';
import axios from 'axios';
import InputForm from './components/InputForm';
import ResultTable from './components/ResultTable';
import ErrorBanner from './components/ErrorBanner';
import LoadingIndicator from './components/LoadingIndicator';

function App() {
    const [results, setResults] = useState(null);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);
    const [dataType, setDataType] = useState('domain');

    const handleSubmit = async ({ domainName, dataType }) => {
        setLoading(true);
        setError(null);
        setResults(null);
        setDataType(dataType);

        try {
            const response = await axios.post('http://localhost:8000/api/whois', {
                domain_name: domainName,
                data_type: dataType
            });
            setResults(response.data);
        } catch (error) {
            if (error.response) {
                // The request was made and the server responded with a status code
                // that falls out of the range of 2xx
                setError(error.response.data.detail || 'An error occurred');
            } else if (error.request) {
                // The request was made but no response was received
                setError('No response from server');
            } else {
                // Something happened in setting up the request that triggered an Error
                setError('Error setting up request');
            }
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-gray-100">
            <div className="container mx-auto px-4 py-8">
                <h1 className="text-3xl font-bold mb-6 text-center text-gray-800">WHOIS Domain Lookup</h1>
                <InputForm onSubmit={handleSubmit} />

                {loading && <LoadingIndicator />}

                {error && <ErrorBanner message={error} />}

                {results && <ResultTable data={results} type={dataType} />}
            </div>
        </div>
    );
}

export default App;