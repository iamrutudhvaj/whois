import React from 'react';

function LoadingIndicator() {
    return (
        <div className="flex justify-center items-center my-6">
            <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
            <p className="ml-3 text-lg">Loading...</p>
        </div>
    );
}

export default LoadingIndicator;